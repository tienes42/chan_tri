/* HỌC ĐỂ LÀM GÌ — API helper
   Existing pages remain unchanged. New pages/components can import/use this.
*/
window.HOC_API_BASE = window.HOC_API_BASE || "http://127.0.0.1:8000/api";

async function hocApi(path, options = {}) {
    const response = await fetch(`${window.HOC_API_BASE}${path}`, {
        headers: {
            "Content-Type": "application/json",
            ...(options.headers || {})
        },
        ...options
    });

    if (!response.ok) {
        const message = await response.text();
        throw new Error(`API ${response.status}: ${message}`);
    }

    return response.json();
}

window.hocApi = hocApi;
