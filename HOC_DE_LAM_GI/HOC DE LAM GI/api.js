const HOC_API_BASE = window.HOC_API_BASE || 'http://127.0.0.1:8000/api';
async function hocApi(path, options={}) {
  const response = await fetch(`${HOC_API_BASE}${path}`, {
    ...options,
    headers: {'Content-Type':'application/json', ...(options.headers||{})}
  });
  if (!response.ok) throw new Error(`API error ${response.status}`);
  return response.json();
}
