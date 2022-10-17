import React, { useEffect } from 'react';

const MyBooks = () => {
    useEffect(() => {
        document.title = 'My Books';
    });    return (
        <div>
            <p>These are my books...</p>
        </div>
    );
};

export default MyBooks;