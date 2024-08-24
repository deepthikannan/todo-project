import React from 'react';

function App() {
    const tasks = ["Task 1", "Task 2", "Task 3"];

    return (
        <div>
            <h1>My To-Do List</h1>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>{task}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
