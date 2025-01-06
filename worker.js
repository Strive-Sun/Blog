addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)
  
  // 处理静态文件
  if (url.pathname.startsWith('/static/')) {
    const response = await fetch(request)
    if (response.ok) {
      return response
    }
  }

  // 处理 Django 应用请求
  const djangoResponse = await fetch('http://127.0.0.1:8000' + url.pathname + url.search, {
    method: request.method,
    headers: request.headers,
    body: request.body
  })

  return djangoResponse
} 