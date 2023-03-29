import React from 'react'

const NavbarMenu = () => {
  return (
    <header>
      <nav>
        <div class="nav-wrapper">
          <a href="#" class="brand-logo">Презентація бізнес проектів</a>
          <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
          <ul class="right hide-on-med-and-down">
            <li><a href="https://martinschrader.pythonanywhere.com">RentalProject</a></li>
          </ul>
        </div>
      </nav>
    </header>
  )
}

export default NavbarMenu