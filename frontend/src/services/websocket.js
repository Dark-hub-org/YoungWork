class WebSocketComponent {
    constructor(path, onOpen, onMessage) {
        this.path = path;
        this.onOpen = onOpen || (() => {});
        this.onMessage = onMessage || (() => {});
        this.websocket = null;

        this.initWebSocket();
    }

    initWebSocket() {
        this.websocket = new WebSocket(this.path);

        this.websocket.onopen = () => {
            this.onOpen();
        };

        this.websocket.onmessage = (event) => {
            this.onMessage(event.data);
        };

        this.websocket.onerror = (error) => {
            console.error('WebSocket Error:', error);
        };
    }

    send(message) {
        if (this.websocket.readyState === WebSocket.OPEN) {
            this.websocket.send(message);
        } else {
            console.error('WebSocket is not open. Unable to send message:', message);
        }
    }

    close() {
        if (this.websocket) {
            this.websocket.close();
        }
    }
}


export default WebSocketComponent


