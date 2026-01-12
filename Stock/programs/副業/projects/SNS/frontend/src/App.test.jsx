import React from 'react';

export default function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>テストページ</h1>
      <p>このページが表示されていれば、Reactは正常に動作しています。</p>
      <p>現在時刻: {new Date().toLocaleString()}</p>
    </div>
  );
}
