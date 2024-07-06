import React from 'react';

function Results({ results }) {
  return (
    <div>
      <h2>Results</h2>
      <p>You scored {results.score} out of {results.total}</p>
    </div>
  );
}

export default Results;
