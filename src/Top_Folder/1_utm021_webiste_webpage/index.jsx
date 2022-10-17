import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import ReactDOM from 'react-dom/client';

import App from '../../App.js';

import Layout from '../0_Component_Folder/Layouts/utm021_website_layout';

import Home from './Home';
import Contact from './Contact';
import Content_Upload from './Content_Upload';
import NoPage from './NoPage';

const Webpages = () => {
    return (
        <Router>
            <Layout>
                <Route exact path="/" component={Home} />
                <Route path="./Contact.jsx" component={Contact} />
                <Route path="./Content_Upload.jsx" component={Content_Upload} />
                <Route path="./NoPage.jsx" component={NoPage} />
            </Layout>
        </Router>
    )
}

export default Webpages;

const root = ReactDOM.createRoot(document.getElementById('root'));
const element = <h1>Hello, world</h1>;
root.render(
    <App/>
);