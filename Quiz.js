import React, { useState } from 'react';

function Quiz({ quiz, onSubmit }) {
  const [answers, setAnswers] = useState(Array(quiz.questions.length).fill(''));

  const handleChange = (index, value) => {
    const newAnswers = [...answers];
    newAnswers[index] = value;
    setAnswers(newAnswers);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(answers);
  };

  return (
    <form onSubmit={handleSubmit}>
      {quiz.questions.map((question, index) => (
        <div key={question.id}>
          <h2>{question.title}</h2>
          {Object.entries(question.answers).map(([key, value]) => (
            <div key={key}>
              <label>
                <input
                  type="radio"
                  name={`question-${index}`}
                  value={key}
                  checked={answers[index] === key}
                  onChange={() => handleChange(index, key)}
                />
                {value}
              </label>
            </div>
          ))}
        </div>
      ))}
      <button type="submit">Submit</button>
    </form>
  );
}

export default Quiz;
