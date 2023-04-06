import React from 'react'
import M from 'materialize-css/dist/js/materialize.min.js';
import 'materialize-css/dist/css/materialize.min.css';
import { useEffect } from 'react';


const ReclamBlock = () => {

  useEffect( () => {
    const parallax = document.querySelector('.parallax');
    M.Parallax.init(parallax);
  }, []);

  return (
    <div className="parallax-container">
        <div className="parallax">
            <img src={require('./bg.png')}/>
        </div>
        <div className="row header-text">
            <h1 className="center-align white-text">Аґенція нерухомості</h1>
            <h5 className="center-align white-text">Знайдемо для Вас ідеальну домівку</h5>
        </div>
    </div>
  )
}

export default ReclamBlock