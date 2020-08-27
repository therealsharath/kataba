import React, { useState, useEffect } from 'react';
import AnswerCard from './AnswerCard.jsx';
import './css/Answers.css';

function Answers(props) {
    const[data, setData] = useState([])

    useEffect(() => {
        if(props.check) {
            var axios = require('axios');

            var config = {
            method: 'get',
            url: 'http://127.0.0.1:8000/api/',
            headers: { 
                'Content-Type': 'application/json'
            }
            };
            axios(config)
            .then(function (response) {
                setData(response.data)
                props.setCheck(false)
            })
            .catch(function (error) {
            console.log(error);
            });
        }
    })
    
    return (
    <div className="AnswerContainer">
        { 
            data && data.map(answer =>
                <AnswerCard question={answer.user_question} answer={answer.model_answer} score={answer.confidence_score}/>
            )
        }
    </div>
    );
}

export default Answers;