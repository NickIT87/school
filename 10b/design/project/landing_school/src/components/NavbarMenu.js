import React from 'react';
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
        <div className="nav-wrapper">
          <a href="#" className="brand-logo">Аґенція нерухомості</a>
          <a href="#" data-target="mobile-demo" className="sidenav-trigger"><i className="material-icons">menu</i></a>
          <ul className="right hide-on-med-and-down">
            <li><a href="https://martinschrader.pythonanywhere.com">RentalProject</a></li>
          </ul>
        </div>
      </nav>

      {/* Мобильное навигационное меню */}
      <ul className="sidenav" id="mobile-demo">
        <li><a href="https://martinschrader.pythonanywhere.com">RentalProject</a></li>
      </ul>
    </header>
  )
}

export default NavbarMenu