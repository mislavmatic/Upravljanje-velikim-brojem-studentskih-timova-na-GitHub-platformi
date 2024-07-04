
import './App.css';
import Sidebar from './components/sidebar';
import React, { useState } from 'react';


function App() {
  const [selectedGroup, setSelectedGroup] = useState(null);

  return (
    <div className="App">
      <Sidebar setSelectedGroup={setSelectedGroup} />
      {selectedGroup && (
        <div className="group-info">
          <h2>{selectedGroup.name_g}</h2>
          <p>GitHub: <a href={selectedGroup.github}>{selectedGroup.github}</a></p>
          <p>Zadatak: {selectedGroup.name_zad}</p>
          <p>Demos: {selectedGroup.name_demos}</p>          
          <div>Studenti: <div style={{ marginLeft: '2vh' }}>
                          {selectedGroup.students.map(student => (
                            <div key={student.s_email} className="student">
                              <p style={{ width: '10vw', display: 'inline-block', marginRight: "1vw"}}>{student.name}</p>
                              <p style={{ width: '10vw', display: 'inline-block', marginRight: "1vw"}}>{student.stud_email}</p>
                              <p style={{ width: '10vw', display: 'inline-block', marginRight: "1vw"}}>{student.is_leader ? "(voditelj)" : ""}</p>
                            </div>
                          ))} 
                        </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
