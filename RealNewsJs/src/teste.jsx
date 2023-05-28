import { useEffect, useState } from 'react';

function App() {
  const [scrapedData, setScrapedData] = useState(null);

  useEffect(() => {
    fetch('Python/RealNewsPy/RealNewsPy/spiders/send_func.py')
      .then(response => response.json())
      .then(data => setScrapedData(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      {scrapedData ? (
        <div>
          <h2>Data Scraped:</h2>
          <pre>{JSON.stringify(scrapedData, null, 2)}</pre>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
