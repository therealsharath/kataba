import React, { useState } from 'react';
import './css/Navbar.css';
import logo from './resources/logo.png';

function Navbar(){
    const[kataba, setKataba] = useState('active');
    const[about, setAbout] = useState('icon');
    const[team, setTeam] = useState('icon');

    const handleClick = (e) => {
        if (e == 'team') {
            setKataba('icon');
            setAbout('icon');
            setTeam('active');
        } else if(e == 'about') {
            setKataba('icon');
            setAbout('active');
            setTeam('icon');
        } else {
            setKataba('active');
            setAbout('icon');
            setTeam('icon');
        }
    }
    return(
        <div className="navbarContainer">
            <img src={logo} className="logo"/>
            <div>
                <a href="#" className={kataba} onClick={() => handleClick('kataba')}>Product</a>
                <a href="#" className={about} onClick={() => handleClick('about')}>About</a>
                <a href="#" className={team} onClick={() => handleClick('team')}>Our Team</a>
            </div>
        </div>
    )
}

export default Navbar;