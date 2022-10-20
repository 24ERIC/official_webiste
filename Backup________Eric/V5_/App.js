import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import { Home } from "./pages/index";
import SigninPage from "./pages/signin";

// import {Link} from 'react-router-dom'
// <Link to={`/user`} >


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" component={Home} />
        <Route path="/signin" component={SigninPage} />
      </Routes>
    </Router>
  );
}

export default App;
