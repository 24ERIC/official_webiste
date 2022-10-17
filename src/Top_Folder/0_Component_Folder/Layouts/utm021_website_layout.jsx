import React from 'react';
import Header from '../Headers/utm021_website_Header';
import Navigation from '../Navigation/utm021_website_Navigation';

const Layout = ({ children }) => {
    return (
    <React.Fragment>
        <Header />
        <div className="navigationWrapper">
            <Navigation />
            <main>{children}</main>
        </div>
    </React.Fragment>
    );
};


export default Layout;