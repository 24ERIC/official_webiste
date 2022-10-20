import React from 'react';
import ReactDOM from 'react-dom'
import App from './App';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   // <React.StrictMode>
//     <App />
// );

ReactDOM.unstable_createRoot(document.getElementById('root')).render(<App />);