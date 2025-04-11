document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing chat...');
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    function addMessage(message, isUser) {
        console.log('Adding message:', message, 'isUser:', isUser);
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
        messageDiv.innerHTML = `<p>${message}</p>`;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        console.log('Attempting to send message:', message);
        
        if (!message) {
            console.log('Empty message, not sending');
            return;
        }

        // Add user message to chat
        addMessage(message, true);
        userInput.value = '';

        try {
            console.log('Sending request to /chat endpoint');
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log('Received response:', data);
            addMessage(data.response, false);
        } catch (error) {
            console.error('Error sending message:', error);
            addMessage('Sorry, there was an error processing your message. Please try again.', false);
        }
    }

    // Event listeners
    sendButton.addEventListener('click', () => {
        console.log('Send button clicked');
        sendMessage();
    });

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            console.log('Enter key pressed');
            sendMessage();
        }
    });

    console.log('Chat initialization complete');
}); 