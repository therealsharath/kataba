import React, { useState, useEffect } from 'react';
import Recorder from  './Recorder.jsx';
import Questions from './Questions.jsx';
import Answers from './Answers.jsx';
import './css/Kataba.css';

function Kataba() {
    const[newQuestion, setNewQuestion] = useState(false)
    const[score, setScore] = useState(90);
    const[check, setCheck] = useState(true);
    const[user, setUser] = useState("GUEST USER")

    const handleQuestionSubmit = () => {
        setNewQuestion(!newQuestion)
        setCheck(true);
    }

    return (
        <div className="katabaContainer">
            <div className="mainIntro">
                <font className="subtitle">WELCOME, <font className="title">{user}!</font></font>
                <font className="subtitle">WOULD YOU LIKE TO START A LECTURE?</font>
            </div>
            <Recorder handleSubmit={handleQuestionSubmit} setCheck={setCheck} newQuestion={newQuestion} setNewQuestion={setNewQuestion}/>
            <div className="title">
                <font>Questions</font>
            </div>
            <Answers check={check} setCheck={setCheck}/>
        </div>
    );
}

export default Kataba;