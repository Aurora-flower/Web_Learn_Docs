// 向主线程发送一条消息
self.postMessage('Hello from worker');

// 定义了一个 message 事件监听器，当接收到来自主线程的消息时，会输出到控制台，并向主线程发送一条响应。
self.addEventListener('message', (event) => {
    console.log(`Received message from main thread: ${event.data}`);
    self.postMessage('Message received');
});

