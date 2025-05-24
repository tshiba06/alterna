import React from 'react';
import BaseCard from './BaseCard';

interface SbiBenefitSystemCardProps {
  total: number;
  loading: boolean;
  onClickUpdate: () => void;
}

const SbiBenefitSystemCard: React.FC<SbiBenefitSystemCardProps> = ({ total, loading, onClickUpdate }) => {
  return (
    <BaseCard
      title="SBIベネフィットシステムズ"
      bgColor="#2ea2ed"
      total={total}
      loading={loading}
      onClickUpdate={onClickUpdate}
    />
  );
};

export default SbiBenefitSystemCard;
