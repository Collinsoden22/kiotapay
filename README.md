# Project Title

## Table of Contents

- [About](#about)
- [App URLS](#links)
- [Solutions](#responses)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This is a task which require:
- Building a flask RESTful API with at least two endpoints that returns data from Postgres SQL.
- Building a React Todo List App that demonstrates react component inheritance using hooks.

## App URLS: <a name = "links"> </a>
- [React App](https://kiotapay-git-master-collinsoden.vercel.app/)
- [Flask API](https://collinsoden.pythonanywhere.com/api/v1/)

## Answers to Questions <a name = "responses"></a>

### How is React different from Angular?
- React is a Javascript library which uses one way binding and virtual DOM. Angular is a frontend framework which uses two-way data binding and real DOM. React, due to its smaller bundle size, is faster than angular.

### What is the virtual DOM?
- The virtual DOM is a lightweight DOM. In a virtual DOM, two render trees are compared and the actual (real) DOM is updated with the element changed. When an element is updated, react takes and compares snapshots before and snapshot after the update, then replaces the actual DOM with the change noticed.

### What are props in React?
- Props, implying 'properties', are a type of objects where the values of attibutes of a tag are stored. They are read only components.

### What are the differences between state and props?
- State is a locally owned component and it is updated by the component itself, props are owned by a parent, they are read-only, props give components the ability to recieve data from parent components in the form of props (properties)

### What do you understand by the term CORS?
- CORS: Cross-Origin Resource Sharing, is an HTTP header based mechanism that allows resource sharing to another domain.

## Getting Started <a name = "getting_started"></a>

To test the api, clone this repository, through your CLI, navigate to `./flask_api/` and run `python3 main.py` and then `python3 test.py`.

### Prerequisites
To run this app, ensure you already have the following dependencies installed:
- [Python3](https://python.org)
- [Postgres](https://www.postgresql.org)


## Usage <a name = "usage"></a>

Add notes about how to use the system.
