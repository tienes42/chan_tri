(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const input=$('expression'), result=$('result'), error=$('error');
  let angleMode='DEG', ans=0, memory=null, shift=false, alpha=false;
  const vars={A:0,B:0,C:0,D:0,E:0,F:0,x:0,y:0};
  const history=[];
  const mathReady=()=>typeof window.math!=='undefined';
  const showError=m=>{error.textContent=m||'';};
  function insertText(text){const s=input.selectionStart??input.value.length,e=input.selectionEnd??s;input.setRangeText(text,s,e,'end');input.focus();showError('');preview();}
  function evaluate(expr, extra={}){
    if(!mathReady()) throw Error('Không tải được thư viện toán học. Hãy kiểm tra Internet rồi tải lại.');
    let source=String(expr).trim(); if(!source)return 0;
    source=source.replace(/×/g,'*').replace(/÷/g,'/').replace(/−/g,'-').replace(/π/g,'pi').replace(/\bAns\b/g,'('+String(ans)+')').replace(/\bnCr\s*\(/g,'nCr(').replace(/\bnPr\s*\(/g,'nPr(');
    const toRad=x=>angleMode==='DEG'?Number(x)*Math.PI/180:Number(x), fromRad=x=>angleMode==='DEG'?Number(x)*180/Math.PI:Number(x);
    const factorial=n=>{n=Number(n);if(!Number.isInteger(n)||n<0||n>170)throw Error('Giai thừa chỉ nhận số nguyên từ 0 đến 170.');let v=1;for(let i=2;i<=n;i++)v*=i;return v;};
    const choose=(n,r)=>{n=Number(n);r=Number(r);if(!Number.isInteger(n)||!Number.isInteger(r)||n<0||r<0||r>n)throw Error('nCr cần số nguyên n ≥ r ≥ 0.');r=Math.min(r,n-r);let v=1;for(let i=1;i<=r;i++)v=v*(n-r+i)/i;return v;};
    const scope={pi:Math.PI,e:Math.E,Ans:ans,...vars,...extra,
      sin:x=>Math.sin(toRad(x)),cos:x=>Math.cos(toRad(x)),tan:x=>{const r=toRad(x);if(Math.abs(Math.cos(r))<1e-14)throw Error('tan không xác định tại góc này.');return Math.tan(r);},
      asin:x=>fromRad(Math.asin(Number(x))),acos:x=>fromRad(Math.acos(Number(x))),atan:x=>fromRad(Math.atan(Number(x))),
      log:x=>Math.log10(Number(x)),ln:x=>Math.log(Number(x)),sqrt:x=>Math.sqrt(Number(x)),cbrt:x=>Math.cbrt(Number(x)),abs:x=>Math.abs(Number(x)),
      exp:x=>Math.exp(Number(x)),floor:x=>Math.floor(Number(x)),ceil:x=>Math.ceil(Number(x)),round:x=>Math.round(Number(x)),
      factorial,nCr:choose,nPr:(n,r)=>choose(n,r)*factorial(r), sign:x=>Math.sign(Number(x))};
    const node=math.parse(source), value=node.compile().evaluate(scope);
    if(typeof value==='number'&&!Number.isFinite(value))throw Error('Kết quả không xác định trong tập số thực.');
    if(value===undefined||typeof value==='function')throw Error('Biểu thức chưa hợp lệ.');
    return value;
  }
  function format(v){if(typeof v==='number'){if(Object.is(v,-0))v=0;return Number(v.toPrecision(12)).toString();}if(v&&typeof v.toString==='function')return v.toString({precision:10});return String(v);}
  function preview(){if(!input.value.trim()){result.textContent='0';showError('');return;}try{result.textContent=format(evaluate(input.value));showError('');}catch(e){result.textContent='…';}}
  function calculate(){try{const expr=input.value.trim();if(!expr)return;const v=evaluate(expr),out=format(v);if(typeof v==='number')ans=v;result.textContent=out;showError('');history.unshift({expression:expr,result:out});if(history.length>50)history.pop();renderHistory();input.value=out;input.focus();input.setSelectionRange(input.value.length,input.value.length);}catch(e){showError(e.message||'Không thể tính biểu thức này.');}}
  function renderHistory(){const list=$('historyList');list.replaceChildren();if(!history.length){const p=document.createElement('p');p.className='empty-history';p.textContent='Các phép tính của bạn sẽ xuất hiện ở đây.';list.append(p);return;}history.forEach(it=>{const b=document.createElement('button');b.className='history-item';b.type='button';const ex=document.createElement('div');ex.className='history-expression';ex.textContent=it.expression;const val=document.createElement('div');val.className='history-result';val.textContent='= '+it.result;b.append(ex,val);b.addEventListener('click',()=>{input.value=it.expression;preview();input.focus();});list.append(b);});}
  function syncFlags(){ $('shiftKey').classList.toggle('active',shift);$('alphaKey').classList.toggle('active',alpha);$('shiftStatus').textContent='SHIFT: '+(shift?'ON':'OFF')+(alpha?' · ALPHA: ON':'');document.querySelectorAll('[data-shift]').forEach(b=>b.textContent=shift?(b.dataset.shift.replace('(','⁻¹')):b.dataset.insert.replace('(','').replace('sqrt','√')); }
  function modePanel(){const mode=$('modeSelect').value,p=$('modePanel');p.hidden=mode==='calculate';p.replaceChildren();if(mode==='calculate')return;
    const add=(tag,attrs={},text='')=>{const el=document.createElement(tag);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,v));if(text)el.textContent=text;return el;};
    const field=(label,id,value)=>{const l=add('label',{},label),i=add('input',{id,value,type:'text'});l.append(i);return l;};
    const button=(text,fn)=>{const b=add('button',{type:'button'},text);b.addEventListener('click',fn);return b;};
    const out=add('div',{class:'panel-output',id:'modeOutput'},'');
    if(mode==='equation'){
      p.append(add('div',{},'Phương trình bậc hai: ax² + bx + c = 0'),add('div',{class:'panel-grid'}));const g=p.querySelector('.panel-grid');g.append(field('Hệ số a','eqA','1'),field('Hệ số b','eqB','-3'),field('Hệ số c','eqC','2'));
      p.append(button('Giải phương trình',()=>{try{const a=Number($('eqA').value),b=Number($('eqB').value),c=Number($('eqC').value);if(![a,b,c].every(Number.isFinite)||a===0)throw Error('a phải khác 0 và các hệ số phải là số.');const d=b*b-4*a*c;let s;if(d<0)s=`Δ = ${format(d)} < 0\nKhông có nghiệm thực. Nghiệm phức: x₁ = ${format(-b/(2*a))} + ${format(Math.sqrt(-d)/(2*a))}i; x₂ = ${format(-b/(2*a))} − ${format(Math.sqrt(-d)/(2*a))}i`;else if(d===0)s=`Δ = 0\nx = ${format(-b/(2*a))}`;else s=`Δ = ${format(d)}\nx₁ = ${format((-b+Math.sqrt(d))/(2*a))}\nx₂ = ${format((-b-Math.sqrt(d))/(2*a))}`;$('modeOutput').textContent=s;}catch(e){$('modeOutput').textContent=e.message;}}));
      p.append(add('div',{},'Hệ 2 phương trình: a₁x + b₁y = c₁; a₂x + b₂y = c₂'));const g2=add('div',{class:'panel-grid'});[['hA1','a₁','1'],['hB1','b₁','1'],['hC1','c₁','5'],['hA2','a₂','1'],['hB2','b₂','-1'],['hC2','c₂','1']].forEach(([id,l,v])=>g2.append(field(l,id,v)));p.append(g2,button('Giải hệ',()=>{const [a,b,c,d,e,f]=['hA1','hB1','hC1','hA2','hB2','hC2'].map(id=>Number($(id).value));const det=a*e-b*d;$('modeOutput').textContent=Math.abs(det)<1e-12?'Hệ không có nghiệm duy nhất.':`x = ${format((c*e-b*f)/det)}\ny = ${format((a*f-c*d)/det)}`;}),out);
    } else if(mode==='table'){
      p.append(field('Hàm f(x)','tableExpr','x^2'),add('div',{class:'panel-grid'}));const g=p.querySelector('.panel-grid');g.append(field('x bắt đầu','tableStart','-5'),field('x kết thúc','tableEnd','5'),field('Bước','tableStep','1'));p.append(button('Tạo bảng',()=>{try{const start=Number($('tableStart').value),end=Number($('tableEnd').value),step=Number($('tableStep').value);if(!Number.isFinite(start+end+step)||step<=0||end<start)throw Error('Khoảng hoặc bước không hợp lệ.');if((end-start)/step>200)throw Error('Tối đa 201 dòng mỗi bảng.');const rows=[];for(let x=start;x<=end+step*1e-9;x+=step)rows.push(`x = ${format(x)}   f(x) = ${format(evaluate($('tableExpr').value,{x}))}`);$('modeOutput').textContent=rows.join('\n');}catch(e){$('modeOutput').textContent=e.message;}}),out);
    } else if(mode==='statistics'){
      p.append(add('div',{},'Nhập các giá trị xᵢ và tần số nᵢ theo cùng thứ tự, cách nhau bằng dấu phẩy hoặc khoảng trắng. Có thể bỏ trống tần số để nhập dữ liệu thô.'),field('Giá trị xᵢ','statsData','1, 2, 3, 4, 5'),field('Tần số nᵢ (để trống nếu nhập dữ liệu thô)','statsFreq','2, 3, 4, 2, 1'),button('Phân tích bảng tần số',()=>{try{
        const parseList=text=>text.trim().split(/[\s,;]+/).filter(Boolean).map(Number);
        const values=parseList($('statsData').value), freqText=$('statsFreq').value.trim();
        if(!values.length||values.some(n=>!Number.isFinite(n)))throw Error('Danh sách giá trị xᵢ không hợp lệ.');
        let frequencies;
        if(!freqText){frequencies=values.map(()=>1);}else{
          frequencies=parseList(freqText);
          if(frequencies.length!==values.length)throw Error('Số tần số phải bằng số giá trị xᵢ.');
          if(frequencies.some(n=>!Number.isInteger(n)||n<0))throw Error('Tần số phải là số nguyên không âm.');
        }
        const pairs=values.map((x,i)=>({x,f:frequencies[i]})).filter(r=>r.f>0).sort((a,b)=>a.x-b.x);
        if(!pairs.length)throw Error('Tổng tần số phải lớn hơn 0.');
        const n=pairs.reduce((s,r)=>s+r.f,0);
        if(n>1000000)throw Error('Tổng tần số tối đa là 1.000.000 để tránh xử lý quá tải.');
        const sum=pairs.reduce((s,r)=>s+r.x*r.f,0), mean=sum/n;
        const ss=pairs.reduce((s,r)=>s+r.f*(r.x-mean)**2,0);
        const pickAt=idx=>{let cumulative=0;for(const r of pairs){cumulative+=r.f;if(idx<cumulative)return r.x;}return pairs[pairs.length-1].x;};
        const median=n%2?pickAt(Math.floor(n/2)):(pickAt(n/2-1)+pickAt(n/2))/2;
        const maxFreq=Math.max(...pairs.map(r=>r.f)), modes=pairs.filter(r=>r.f===maxFreq).map(r=>r.x);
        const table=pairs.map(r=>`${format(r.x)}\t${r.f}\t${r.f/n===0?'0':format(r.f/n)}\t${format(r.x*r.f)}`).join('\n');
        $('modeOutput').textContent=`BẢNG TẦN SỐ\nxᵢ\tnᵢ\ttần suất\txᵢ·nᵢ\n${table}\n──────────────\nTổng số quan sát n = ${n}\nΣxᵢnᵢ = ${format(sum)}\nTrung bình x̄ = ${format(mean)}\nTrung vị = ${format(median)}\nMốt = ${modes.map(format).join(', ')} (tần số ${maxFreq})\nMin = ${format(pairs[0].x)}\nMax = ${format(pairs[pairs.length-1].x)}\nPhương sai tổng thể σ² = ${format(ss/n)}\nĐộ lệch chuẩn tổng thể σ = ${format(Math.sqrt(ss/n))}\nPhương sai mẫu s² = ${n>1?format(ss/(n-1)):'—'}\nĐộ lệch chuẩn mẫu s = ${n>1?format(Math.sqrt(ss/(n-1))):'—'}`;
      }catch(e){$('modeOutput').textContent=e.message||'Dữ liệu thống kê không hợp lệ.';}}),out);
    } else if(mode==='matrix'){
      p.append(add('div',{},'Nhập ma trận vuông 2×2 hoặc 3×3; mỗi hàng một dòng, các phần tử cách nhau bằng dấu cách hoặc dấu phẩy.'),field('Ma trận','matrixData','1, 2\n3, 4'),button('Tính định thức và nghịch đảo',()=>{try{const rows=$('matrixData').value.trim().split(/\n/).map(r=>r.trim().split(/[\s,;]+/).map(Number));const n=rows.length;if(![2,3].includes(n)||rows.some(r=>r.length!==n||r.some(v=>!Number.isFinite(v))))throw Error('Chỉ hỗ trợ ma trận vuông 2×2 hoặc 3×3.');let det;if(n===2)det=rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0];else det=rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])-rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])+rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0]);let text=`det(A) = ${format(det)}`;if(Math.abs(det)<1e-12)text+='\nMa trận suy biến, không có nghịch đảo.';else{const inv=math.inv(rows).toArray();text+='\nA⁻¹ =\n'+inv.map(r=>r.map(format).join('\t')).join('\n');}$('modeOutput').textContent=text;}catch(e){$('modeOutput').textContent=e.message;}}),out);
    }
  }
  document.querySelectorAll('[data-insert]').forEach(b=>b.addEventListener('click',()=>{let text=b.dataset.insert;if(alpha&&/^[A-F]$/.test(text)){alpha=false;syncFlags();}if(shift&&b.dataset.shift){text=b.dataset.shift;shift=false;syncFlags();}insertText(text);}));
  document.querySelectorAll('[data-action]').forEach(b=>b.addEventListener('click',()=>{const a=b.dataset.action;if(a==='clear'){input.value='';result.textContent='0';showError('');input.focus();}else if(a==='backspace'){const s=input.selectionStart??input.value.length,e=input.selectionEnd??s;input.setRangeText('',s===e?Math.max(0,s-1):s,e,'end');preview();input.focus();}else if(a==='equals')calculate();else if(a==='shift'){shift=!shift;syncFlags();}else if(a==='alpha'){alpha=!alpha;shift=false;syncFlags();}else if(a==='memory-store'){try{memory=Number(evaluate(input.value));if(!Number.isFinite(memory))throw Error();memoryStatus.textContent='M: '+format(memory);showError('Đã lưu giá trị vào M.');}catch(_){showError('Hãy nhập một giá trị hợp lệ trước khi STO.');}}else if(a==='memory-recall'){if(memory===null)showError('Bộ nhớ M đang trống.');else insertText(String(memory));}else if(a==='memory-add'){try{memory=(memory||0)+Number(evaluate(input.value));memoryStatus.textContent='M: '+format(memory);showError('Đã cộng kết quả vào M.');}catch(_){showError('Không có kết quả hợp lệ để cộng vào M.');}}}));
  $('angleToggle').addEventListener('click',()=>{angleMode=angleMode==='DEG'?'RAD':'DEG';$('angleMode').textContent=angleMode;preview();});$('clearHistory').addEventListener('click',()=>{history.length=0;renderHistory();});$('modeSelect').addEventListener('change',modePanel);
  input.addEventListener('input',preview);input.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();calculate();}if(e.key==='Escape'){input.value='';preview();}});document.addEventListener('keydown',e=>{if(e.key==='F9'){e.preventDefault();$('angleToggle').click();}if(e.key==='F2'){e.preventDefault();$('shiftKey').click();}});
  function selfTest(){if(!mathReady())return;const tests=[['2+3*4',14],['sqrt(16)',4],['sin(30)',.5],['log(100)',2],['5!',120],['nCr(5,2)',10],['2^10',1024]];const failures=[];tests.forEach(([ex,expected])=>{try{const actual=Number(evaluate(ex));if(Math.abs(actual-expected)>1e-8)failures.push(ex);}catch(_){failures.push(ex);}});if(failures.length)console.warn('HDLJ calculator tests failed:',failures);else console.info('HDLJ calculator smoke tests passed:',tests.length);}
  renderHistory();syncFlags();modePanel();memoryStatus.textContent='M: —';selfTest();
})();
