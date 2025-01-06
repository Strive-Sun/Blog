(() => {
  var __defProp = Object.defineProperty;
  var __name = (target, value) => __defProp(target, "name", { value, configurable: true });

  // worker.js
  addEventListener("fetch", (event) => {
    event.respondWith(handleRequest(event.request));
  });
  async function handleRequest(request) {
    const url = new URL(request.url);
    if (url.pathname.startsWith("/static/")) {
      const response = await fetch(request);
      if (response.ok) {
        return response;
      }
    }
    const djangoResponse = await fetch("http://127.0.0.1:8000" + url.pathname + url.search, {
      method: request.method,
      headers: request.headers,
      body: request.body
    });
    return djangoResponse;
  }
  __name(handleRequest, "handleRequest");
})();
//# sourceMappingURL=worker.js.map
