import { getAssetFromKV } from '@cloudflare/kv-asset-handler'

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)
  
  try {
    // 构建本地文件路径
    let path = url.pathname
    if (path === '/' || path === '') {
      path = '/index.html'
    }

    // 从构建目录读取文件
    const response = await fetch(`https://raw.githubusercontent.com/Strive-Sun/Blog/main/build${path}`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    // 设置响应头
    const headers = new Headers({
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, HEAD, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    })

    // 根据文件类型设置Content-Type
    const ext = path.split('.').pop().toLowerCase()
    const contentTypes = {
      'html': 'text/html',
      'css': 'text/css',
      'js': 'application/javascript',
      'png': 'image/png',
      'jpg': 'image/jpeg',
      'jpeg': 'image/jpeg',
      'gif': 'image/gif',
      'svg': 'image/svg+xml'
    }
    headers.set('Content-Type', contentTypes[ext] || 'text/plain')

    // 设置缓存控制
    if (path.startsWith('/static/') || path.startsWith('/staticfiles/')) {
      headers.set('Cache-Control', 'public, max-age=31536000')
    } else {
      headers.set('Cache-Control', 'no-cache, no-store, must-revalidate')
    }

    return new Response(response.body, {
      status: 200,
      headers: headers
    })
  } catch (e) {
    return new Response('Page not found', { 
      status: 404,
      headers: {
        'Content-Type': 'text/plain',
        'Access-Control-Allow-Origin': '*'
      }
    })
  }
} 