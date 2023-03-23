import React from 'react'

const NavbarMenu = () => {
  return (
    <header>
      <nav>
        <div class="nav-wrapper">
          <a href="#" class="brand-logo">Агентство недвижимости</a>
          <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
          <ul class="right hide-on-med-and-down">
            <li><a href="#about">О нас</a></li>
            <li><a href="#services">Услуги</a></li>
            <li><a href="#contact">Контакты</a></li>
          </ul>
        </div>
      </nav>
    </header>
  )
}

export default NavbarMenu