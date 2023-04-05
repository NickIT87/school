import './App.css';
import BlockMain from './components/BlockMain';
import NavbarMenu from './components/NavbarMenu';


function App() {
  return (
    <div className="App">
      <NavbarMenu />
      <BlockMain />
      <img src={require('./logo.svg')}/>
    </div>
  );
}

export default App;
