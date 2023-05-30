import { useEffect, useState } from 'react';
import axios from 'axios';

function NewsComponent() {
  const [taskId, setTaskId] = useState(null);
  const [taskStatus, setTaskStatus] = useState(null);
  const [taskResult, setTaskResult] = useState(null);

  useEffect(() => {
    // Função para obter o ID da tarefa de scraping
    const fetchTaskId = async () => {
      try {
        const response = await axios.get('/news');
        setTaskId(response.data.task_id);
      } catch (err) {
        console.error('Erro ao obter o ID da tarefa:', err);
      }
    };

    fetchTaskId();
  }, []);

  useEffect(() => {
    // Função para verificar o status da tarefa e obter o resultado
    const fetchTaskResult = async () => {
      if (taskId) {
        try {
          let status = 'PENDING';
          // Aguarda a conclusão da tarefa de scraping
          while (status === 'PENDING') {
            const response = await axios.get(`/task/${taskId}`);
            status = response.data.status;
            if (status === 'SUCCESS') {
              setTaskResult(response.data.result);
            }
          }

          setTaskStatus(status);
        } catch (error) {
          console.error('Erro ao obter o status da tarefa:', error);
        }
      }
    };

    fetchTaskResult();
  }, [taskId]);

  return (
    <div>
      <h2>Consulta de Notícias</h2>
      {taskStatus === 'PENDING' && <p>A tarefa está em andamento. Aguarde o resultado.</p>}
      {taskStatus === 'SUCCESS' && taskResult && (
        <div>
          <h3>Resultado:</h3>
          <pre>{JSON.stringify(taskResult, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default NewsComponent;
