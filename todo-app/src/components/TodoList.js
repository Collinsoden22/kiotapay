import React, {useState, useEffect} from 'react'
import TodoForm from "./TodoForm";
import Todo from './Todo';

function TodoList() {

    const [todos, setTodos] = useState([]);

    const addTodo = todo => {
        // Serialize text, ignore empty text
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

    const completeTodo = id =>{
        let updatedTodos = todos.map(todo => {
            if (todo.id === id){
                todo.isComplete = !todo.isComplete // Change to `true` if !toggle
            }
            return todo
        });
        setTodos(updatedTodos)
    }

    useEffect (() => {
        localStorage.setItem("todos", JSON.stringify(todos));
      }, [todos]);

      useEffect(() => {
        const storedTodos = JSON.parse(localStorage.getItem("todos"));
        if (storedTodos){
            setTodos(storedTodos)
        }
      }, [todos])

  return (
    <div>
        <h3 className="m-5 justify-content-center text-center"> What are we planning today?</h3>
        <TodoForm onSubmit={addTodo}/>
        <div className="justify-contents-center p-5">
            <Todo
            todos={todos}
            completeTodo={completeTodo}
            removeTodo={removeTodo} />
        </div>

    </div>

  )
}

export default TodoList