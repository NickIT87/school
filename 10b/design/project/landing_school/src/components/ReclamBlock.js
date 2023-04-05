import React from 'react'
import M from 'materialize-css/dist/js/materialize.min.js';
import 'materialize-css/dist/css/materialize.min.css';
import bg from './bg.png';


const ReclamBlock = () => {
  return (
    <div className="parallax-container">
        <div className="parallax">
            <img src={bg} alt="bg" />
            <img src={require('./bg.png')}/>
        </div>
        <div className="row header-text">
            <h1 className="center-align white-text">Агентство недвижимости</h1>
            <h5 className="center-align white-text">Найдем для вас идеальный дом</h5>
        </div>
    </div>
  )
}

export default ReclamBlock