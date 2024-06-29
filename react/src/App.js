
import './App.css';

import Sidebar from './components/sidebar';
import React, { useState } from 'react';


function App() {
  const [selectedGroup, setSelectedGroup] = useState(null);

  return (
    <div className="App">
      {/* <header className="App-header">
        Naslov web aplikacije
      </header> */}
      <Sidebar setSelectedGroup={setSelectedGroup} />
      {selectedGroup && (
        <div className="group-info">
          <h2>{selectedGroup.name_g}</h2>
          <p>GitHub: <a href={selectedGroup.github}>{selectedGroup.github}</a></p>
          <p>Zadatak: {selectedGroup.name_zad}</p>
          {/* <p>Demos: {selectedGroup.name_demos && selectedGroup.name_demos.join(', ')}</p> */}
          <p>Demos: {selectedGroup.name_demos}</p>          
          {/* <p>Students: {selectedGroup.students && selectedGroup.students.join(', ')}</p> */}
          <div>Studenti: <div style={{ marginLeft: '2vh' }}>
                          {selectedGroup.students.map(student => (
                            <p key={student.s_id} className="student">{student.name} {student.is_leader ? "(voditelj)" : ""}</p>
                          ))} 
                        </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
