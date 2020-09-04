import React, { useState, useEffect } from 'react';
import Questions from './Questions.jsx';
import axios from 'axios';
import './css/Recorder.css';

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition
const mic = new SpeechRecognition()

mic.continuous = true
mic.interimResults = true
mic.lang = 'en-US'

function Recorder(props) {
    const [isListening, setIsListening] = useState(false)
    const [note, setNote] = useState(null)

    useEffect(() => {
        handleListen()
    }, [isListening])
    
    const handleListen = () => {
        if (isListening) {
          mic.start()
          mic.onend = () => {
            mic.start()
          }
        } else {
          mic.stop()
          mic.onend = () => {
          }
        }
        mic.onstart = () => {
        }
    
        mic.onresult = event => {
          const transcript = Array.from(event.results)
            .map(result => result[0])
            .map(result => result.transcript)
            .join('')
          setNote(transcript)
          mic.onerror = event => {
            console.log(event.error)
          }
        }
      }
    
      const handleSubmit = () => {
        axios.post(`http://127.0.0.1:8000/api/create-lecture/`, { 
            lecture_id: "00000000",
            lecture_url: "Too broke for cloud storage :p",
            lecture_text: note,
          })
          .catch(err => {
            console.log(err);
          })
        setNote('')
      }

      return (
        <div className="recorderContainer">
          <button className="record" onClick={() => setIsListening(prevState => !prevState)}>
              {!isListening ? <span>🎙️</span> : <span>🛑</span>}
          </button>
          <div className="buttonContainer">
            <button className="button button1" onClick={handleSubmit} disabled={!note}>
              Upload ☝️
            </button>
            <button className="button button1" onClick={() => props.setNewQuestion(!props.newQuestion)}>{props.newQuestion ? "Cancel" : "New Question"}</button>
          </div>
          {props.newQuestion && <Questions handleSubmit={props.handleSubmit} setCheck={props.setCheck}/>}
        </div>
      )
}

export default Recorder;