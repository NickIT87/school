import React from 'react'
import M from 'materialize-css/dist/js/materialize.min.js';
import 'materialize-css/dist/css/materialize.min.css';
import { useEffect } from 'react';


const NavbarMenu = () => {

  useEffect( () => {
    const sidenav = document.querySelector('.sidenav');
    M.Sidenav.init(sidenav);
  }, []);

  return (
    <header>
      <nav>
        <div class="nav-wrapper">
          <a href="#" class="brand-logo">Аґенція нерухомості</a>
          <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
          <ul class="right hide-on-med-and-down">
            <li><a href="https://martinschrader.pythonanywhere.com">RentalProject</a></li>
          </ul>
        </div>
      </nav>

      {/* Мобильное навигационное меню */}
      <ul class="sidenav" id="mobile-demo">
        <li><a href="#about">О нас</a></li>
        <li><a href="#services">Услуги</a></li>
        <li><a href="#contact">Контакты</a></li>
      </ul>
    </header>
  )
}



export default NavbarMenu