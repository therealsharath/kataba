import React, { useState, useEffect } from 'react';
import './css/AnswerCard.css';

function AnswerCard(props) {
    const[scoreColor, setScoreColor] = useState('score1')

    useEffect(() => {
        if(props.score >= 90) {
            setScoreColor('score1')
        } else if (props.score >= 70 && props.score < 90) {
            setScoreColor('score2');
        } else if (props.score >= 50 && props.score < 70) {
            setScoreColor('score3');
        } else {
            setScoreColor('score4')
        }
    })
    return(
        <div className="AnswerCardWrapper">
            <div className="AnswerCard">
                <div className="bunch">
                    <font className="Caption">Question</font>
                    <font className="Content">{props.question}</font>
                </div>
                <div className="bunch">
                    <font className="Caption">Answer</font>
                    <font className="Content">{(props.answer =='') ? "Processing..." : props.answer}</font>
                </div>
                <font className="Caption">Confidence Score: <font className={scoreColor}>{props.score}</font></font>
            </div>
        </div>
    )
}

export default AnswerCard;