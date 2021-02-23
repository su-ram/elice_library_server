import logo from './logo.svg';
import { Container, TextField, Button } from '@material-ui/core';
import './App.css';
import SignIn from './SignIn';
import SignUp from './SignUp';
import { Route } from 'react-router-dom';


function App() {
  return (
    <>
      <Route path="/signin" component={SignIn} />
      <Route path="/signup" component={SignUp} />
    </>
  );
}

export default App;
