import { useState, useEffect } from 'react';
import io from 'socket.io-client';

const socket = io('https://chat-application-gmj4.onrender.com');

export default function Home() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);

  useEffect(() => {
    socket.on('chat-message', (data) => {
      setChat((prev) => [...prev, data]);
    });

    return () => socket.disconnect(); // cleanup on unmount
  }, []);

  const sendMessage = () => {
    if (!message.trim()) return;

    const msg = { text: message, sender: 'You' };
    setChat((prev) => [...prev, msg]);
    socket.emit('chat-message', msg);
    setMessage('');
  };

  return (
    <div style={{ padding: 20, fontFamily: 'Arial' }}>
      <h1>💬 Real-Time Chat</h1>
      <div
        style={{
          marginBottom: 10,
          height: 300,
          overflowY: 'auto',
          border: '1px solid #ccc',
          borderRadius: 6,
          padding: 10,
          background: '#fafafa',
        }}
      >
        {chat.map((msg, i) => (
          <div key={i} style={{ marginBottom: 6 }}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
        placeholder="Type a message..."
        style={{
          width: '70%',
          padding: '8px',
          borderRadius: 4,
          border: '1px solid #ccc',
          marginRight: 10,
        }}
      />
      <button
        onClick={sendMessage}
        style={{
          padding: '8px 16px',
          borderRadius: 4,
          background: '#0070f3',
          color: 'white',
          border: 'none',
          cursor: 'pointer',
        }}
      >
        Send
      </button>
    </div>
  );
}
