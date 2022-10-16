import React from 'react';
import './index.css';
import App from './App';



import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Contact from './Top_Folder/1_utm021_Webiste/Contact';
import Home from './Top_Folder/1_utm021_Webiste/Home';
import NoPage from './Top_Folder/1_utm021_Webiste/NoPage';
import Projects from './Top_Folder/1_utm021_Webiste/Content_Upload';

export default function Appp() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Home />} />
        <Route path="projects" element={<Projects />} />
        <Route path="contact" element={<Contact />} />
        <Route path="*" element={<NoPage />} />
      </Routes>
    </BrowserRouter>
  );
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(

  <App />

);

