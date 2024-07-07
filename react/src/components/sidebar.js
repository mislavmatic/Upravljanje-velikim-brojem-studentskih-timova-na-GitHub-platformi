import React from "react";
import "../App.css"
import { useState } from 'react';
import FileUpload from '../FileUpload';

function Sidebar({ setSelectedGroup }) {
  const [data, setData] = useState(null);
  const [expandedAsistenti, setExpandedAsistenti] = useState({});
  const [expandedGrupe, setExpandedGrupe] = useState({});
//   const [concreteGroup, updateGroup] = useState({});

  const handleGetData = () => {
      fetch('http://localhost:5000/get_data')
          .then(response => response.json())
          .then(data => setData(data))
          .catch(error => console.error('Error:', error));
  };

  const GroupCommitCount = (github) => {
    // console.log(github);
    // fetch(`http://localhost:5000/api/group-commit-count/${github}`)
    //     .then(response => response.json())
    //     .then(concreteGroup => updateGroup(concreteGroup))
    //     .catch(error => console.error('Error fetching commit count:', error));
    return fetch(`http://localhost:5000/api/group-commit-count/${github}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .catch(error => console.error('There has been a problem with your fetch operation:', error));
  };


  const toggleExpandedAsistenti = (id) => {
      setExpandedAsistenti(prevExpanded => {
          const newExpanded = {...prevExpanded};
          newExpanded[id] = !newExpanded[id];
          return newExpanded;
      });
  };

//   const toggleExpandedGrupe = (id) => {
//       setExpandedGrupe(prevExpanded => {
//           const newExpanded = {...prevExpanded};
//           newExpanded[id] = !newExpanded[id];
//           return newExpanded;
//       });
//   };

const toggleExpandedGrupe = (github) => {
    setExpandedGrupe(prevExpanded => {
        const newExpanded = {...prevExpanded};
        newExpanded[github] = !newExpanded[github];
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
                  {expandedAsistenti[assistantIndex] && assistant.groups.map((group) => (
                      <div key={group.github} className="group">
                          <button onClick={() => {
                              toggleExpandedGrupe(group.github);
                              GroupCommitCount(group.github)
                                .then(updateGroup => {
                                    setSelectedGroup(updateGroup);
                                })
                                .catch(e => console.error("Error group update", e));
                            //   setSelectedGroup();
                          }}>
                              {group.name_g}
                          </button>
                          {expandedGrupe[group.github]}
                      </div>
                  ))}
              </div>
          ))}
      </div>
  );



// return (
//     <div className="Sidebar">
//         <FileUpload />
//         <button onClick={handleGetData}>Get Data</button>
//         {data && data.map((assistant) => (
//             <div key={assistant.name_asist} className="assistant">
//                 <button onClick={() => toggleExpandedAsistenti(assistant.name_asist)}>
//                     {assistant.name_asist}
//                 </button>
//                 {expandedAsistenti[assistant.name_asist] && assistant.groups.map((group) => (
//                     <div key={group.github} className="group">
//                         <button onClick={() => {
//                             toggleExpandedGrupe(group.github);
//                             setSelectedGroup(group);
//                         }}>
//                             {group.name_g}
//                         </button>
//                         {expandedGrupe[group.github]}
//                     </div>
//                 ))}
//             </div>
//         ))}
//     </div>
// );
}


export default Sidebar