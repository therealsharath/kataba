import React from 'react';
import { useForm } from 'react-hook-form';
import './css/Questions.css';

function Questions(props) {
    const { register, handleSubmit, reset, errors } = useForm();

    const onSubmit = (data) => {
        console.log(data.question)
        var axios = require('axios');
        var data = JSON.stringify({"lecture_id":"00000000","user_question":data.question,"model_answer":"","confidence_score":null,"answered":false});
        var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/create/',
        headers: { 
            'Content-Type': 'application/json'
        },
        data : data
        };
        axios(config)
        .then(function (response) {
        console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
        console.log(error);
        });

        var config = {
            method: 'post',
            url: 'http://127.0.0.1:8000/api/answer/',
            headers: { 
                'Content-Type': 'application/json'
            }
            };
            axios(config)
            .then(function (response) {
                console.log("Done");
                props.setCheck(true);
            })
            .catch(function (error) {
            console.log(error);
        });
        props.handleSubmit();
        reset('')
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            {/* include validation with required or other standard HTML validation rules */}
            <input name="question" ref={register({ required: true })}/>
            {/* errors will return when field validation fails  */}
            {errors.exampleRequired && <span>This field is required</span>}
            <input className="submitButton button1" type="submit"/>
        </form>
    );
}

export default Questions;
