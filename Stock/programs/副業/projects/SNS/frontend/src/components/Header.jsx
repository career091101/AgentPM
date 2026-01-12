import React from 'react';

export default function Header() {
  return (
    <header className="bg-white shadow-sm">
      <div className="container mx-auto px-4 py-6">
        <h1 className="text-3xl font-bold text-gray-900">
          SNS投稿管理
        </h1>
        <p className="text-sm text-gray-600 mt-1">
          3つの投稿案から選択・編集して承認
        </p>
      </div>
    </header>
  );
}
