import React from 'react';
import Recorder from  './components/Recorder.jsx';
import Questions from './components/Questions';
import './App.css';

function App() {
  return (
    <div className="App">
      <Recorder />
      <Questions/>
    </div>
  );
}

export default App;
