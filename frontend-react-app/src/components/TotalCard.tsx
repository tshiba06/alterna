import { type FC } from 'react';
import BaseCard from './BaseCard';

interface TotalCardProps {
  total: number;
  loading: boolean;
  onClickUpdate: () => void;
}

export const TotalCard: FC<TotalCardProps> = ({ total, loading, onClickUpdate }) => {
  return (
    <BaseCard
      title="Total"
      bgColor="black"
      total={total}
      loading={loading}
      onClickUpdate={onClickUpdate}
    />
  );
};

export default TotalCard;
