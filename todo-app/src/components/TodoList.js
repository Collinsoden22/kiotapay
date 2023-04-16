import React, {useState, useEffect } from 'react'
import TodoForm from "./TodoForm";
import Todo from './Todo';

function TodoList() {
    const initialState = JSON.parse(localStorage.getItem("todos")) || [];
    const [todos, setTodos] = useState(initialState);


    useEffect(() => {
        localStorage.setItem("todos", JSON.stringify(todos))
    }, [todos]);

    const addTodo = todo => {
        if(!todo.text || /^\s*$/.test(todo.text)){
            return
        }
        const newTodos = [todo, ...todos];

        setTodos(newTodos);
    }

    const removeTodo = id => {
        const filteredTodo = [...todos].filter(todo => todo.id !== id)
        setTodos(filteredTodo);
    }

    const clearStorage = e => {
        if(localStorage.getItem("todos") !== null || []){
            localStorage.removeItem("todos");

            const newTodos = [];

            setTodos(newTodos);
        }
      }

    const completeTodo = id =>{
        let updatedTodos = todos.map(todo => {
            if (todo.id === id){
                todo.isComplete = !todo.isComplete // Change to `true` if !toggle
            }
            return todo
        });
        updatedTodos = updatedTodos.sort((a, b) => a.isComplete - b.isComplete);

        setTodos(updatedTodos);
    }

  return (

    <div>
        <h4 className="float-end mt-5">
            <button className="btn btn-outline-danger" onClick={clearStorage}> Reset</button>
        </h4>
        <h3 className="m-5 justify-content-center text-center"> What are we planning today?</h3>
        <TodoForm onSubmit={addTodo}/>
        <div className="justify-contents-center p-5">
            <Todo
            todos={todos}
            completeTodo={completeTodo}
            removeTodo={removeTodo}/>
        </div>

    </div>

  )
}

export default TodoList