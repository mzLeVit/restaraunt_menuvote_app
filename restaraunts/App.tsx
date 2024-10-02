import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import MenuPage from './pages/MenuPage';
import LoginPage from './pages/LoginPage';
import ResultsPage from './pages/ResultsPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" component={LoginPage} />
        <Route path="/menu" component={MenuPage} />
        <Route path="/results" component={ResultsPage} />
      </Switch>
    </Router>
  );
}

export default App;
