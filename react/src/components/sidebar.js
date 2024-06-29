import React from "react";
import "../App.css"

import { useState } from 'react';
import FileUpload from '../FileUpload';

function Sidebar({ setSelectedGroup }) {
  const [data, setData] = useState(null);
  const [expandedAsistenti, setExpandedAsistenti] = useState({});
  const [expandedGrupe, setExpandedGrupe] = useState({});

  const handleGetData = () => {
      fetch('http://localhost:5000/get_data')
          .then(response => response.json())
          .then(data => setData(data))
          .catch(error => console.error('Error:', error));
  };

  const toggleExpandedAsistenti = (id) => {
      setExpandedAsistenti(prevExpanded => {
          const newExpanded = {...prevExpanded};
          newExpanded[id] = !newExpanded[id];
          return newExpanded;
      });
  };

  const toggleExpandedGrupe = (id) => {
      setExpandedGrupe(prevExpanded => {
          const newExpanded = {...prevExpanded};
          newExpanded[id] = !newExpanded[id];
          return newExpanded;
      });
  };

  return (
      <div className="Sidebar">
          <FileUpload />
          <button onClick={handleGetData}>Get Data</button>
          {data && data.map((assistant, assistantIndex) => (
              <div key={assistant.name_asist} className="assistant">
                  <button onClick={() => toggleExpandedAsistenti(assistantIndex)}>
                      {assistant.name_asist}
                  </button>
                  {expandedAsistenti[assistantIndex] && assistant.groups.map((group, groupIndex) => (
                      <div key={group.name_g} className="group">
                          <button onClick={() => {
                              toggleExpandedGrupe(groupIndex);
                              setSelectedGroup(group);
                          }}>
                              {group.name_g}
                          </button>
                          {expandedGrupe[groupIndex]}
                      </div>
                  ))}
              </div>
          ))}
      </div>
  );
}


export default Sidebar