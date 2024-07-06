import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Quiz from './Quiz';
import Results from './Results';

function App() {
  const [quiz, setQuiz] = useState(null);
  const [results, setResults] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/quizzes/1') // Adjust the quiz ID as needed
      .then(response => {
        setQuiz(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the quiz!", error);
      });
  }, []);

  const handleQuizSubmit = (answers) => {
    // Calculate the score
    const score = quiz.questions.reduce((total, question, index) => {
      if (question.correct_answer === answers[index]) {
        return total + 1;
      }
      return total;
    }, 0);

    setResults({ score, total: quiz.questions.length });
  };

  return (
    <div className="App">
      <h1>Quiz</h1>
      {quiz ? (
        results ? (
          <Results results={results} />
        ) : (
          <Quiz quiz={quiz} onSubmit={handleQuizSubmit} />
        )
      ) : (
        <p>Loading quiz...</p>
      )}
    </div>
  );
}

export default App;
