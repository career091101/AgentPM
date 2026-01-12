import React, { useState } from 'react';
import { usePosts } from '../contexts/PostsContext';
import { refinePost } from '../utils/api';
import toast from 'react-hot-toast';

export default function AIRefineTab() {
  const { state, dispatch } = usePosts();
  const [instruction, setInstruction] = useState('');
  const [isRefining, setIsRefining] = useState(false);

  const handleRefine = async () => {
    if (!instruction.trim()) {
      toast.error('修正指示を入力してください');
      return;
    }

    setIsRefining(true);
    try {
      const result = await refinePost({
        variant_num: state.selectedPost.variantNum || '案1',
        instruction,
        session_id: Date.now().toString()
      });

      dispatch({ type: 'UPDATE_DRAFT', payload: result.refined_content });
      toast.success('AI修正が完了しました');
      setInstruction('');
    } catch (error) {
      toast.error('AI修正に失敗しました');
    } finally {
      setIsRefining(false);
    }
  };

  const presets = [
    'もっとカジュアルに',
    '短くまとめて',
    '数字を具体的に',
    'フォーマルに'
  ];

  return (
    <div className="space-y-4">
      {/* プリセットボタン */}
      <div>
        <label className="block text-sm font-medium mb-2">よく使う修正</label>
        <div className="flex flex-wrap gap-2">
          {presets.map((preset) => (
            <button
              key={preset}
              onClick={() => setInstruction(preset)}
              className="px-3 py-1 text-sm bg-gray-100 rounded hover:bg-gray-200"
            >
              {preset}
            </button>
          ))}
        </div>
      </div>

      {/* カスタム指示入力 */}
      <div>
        <label className="block text-sm font-medium mb-2">修正指示</label>
        <textarea
          value={instruction}
          onChange={(e) => setInstruction(e.target.value)}
          className="w-full h-24 p-3 border rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="例: データ整備ではなく、社員教育に変更"
        />
      </div>

      {/* 実行ボタン */}
      <button
        onClick={handleRefine}
        disabled={isRefining}
        className="w-full bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700 disabled:opacity-50"
      >
        {isRefining ? 'AI修正中...' : 'AI修正を実行'}
      </button>

      {/* 修正履歴 */}
      {state.editMode.refineHistory.length > 0 && (
        <div>
          <label className="block text-sm font-medium mb-2">修正履歴</label>
          <div className="space-y-2">
            {state.editMode.refineHistory.map((history, index) => (
              <div key={index} className="p-3 bg-gray-50 rounded text-sm">
                <div className="font-medium text-gray-700">{history.instruction}</div>
                <div className="text-xs text-gray-500 mt-1">{history.timestamp}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
