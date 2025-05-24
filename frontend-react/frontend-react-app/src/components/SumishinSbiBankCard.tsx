import React from 'react';
import BaseCard from './BaseCard';

interface SumishinSbiBankCardProps {
  total: number;
  loading: boolean;
  onClickUpdate: () => void;
}

const SumishinSbiBankCard: React.FC<SumishinSbiBankCardProps> = ({ total, loading, onClickUpdate }) => {
  return (
    <BaseCard
      title="住信SBI銀行"
      bgColor="#0058A0"
      total={total}
      loading={loading}
      onClickUpdate={onClickUpdate}
    />
  );
};

export default SumishinSbiBankCard;
