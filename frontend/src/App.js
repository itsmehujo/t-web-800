import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState(null);
  useEffect(() => {
  fetch(' http://localhost:8000/').then(res => res.json()).then(({message}) => {
      setMessage(message);
    });
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <p>hella</p>
      <p>{message}</p> <br/>

      </header>
    </div>
  );
}

export default App;