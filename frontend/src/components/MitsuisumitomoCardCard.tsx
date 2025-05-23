import { type FC } from 'react';
import BaseCard from './BaseCard';

interface MitsuisumitomoCardCardProps {
  total: number;
  loading: boolean;
  onClickUpdate: () => void;
}

export const MitsuisumitomoCardCard: FC<MitsuisumitomoCardCardProps> = ({ total, loading, onClickUpdate }) => {
  return (
    <BaseCard
      title="三井住友カード"
      bgColor="#004736"
      total={total}
      loading={loading}
      onClickUpdate={onClickUpdate}
    />
  );
};

export default MitsuisumitomoCardCard;
