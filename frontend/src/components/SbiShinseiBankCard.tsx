import { type FC } from 'react';
import BaseCard from './BaseCard';

interface SbiShinseiBankCardProps {
  total: number;
  loading: boolean;
  onClickUpdate: () => void;
}

export const SbiShinseiBankCard: FC<SbiShinseiBankCardProps> = ({ total, loading, onClickUpdate }) => {
  return (
    <BaseCard
      title="SBI新生銀行"
      bgColor="#e8f1f9"
      total={total}
      loading={loading}
      onClickUpdate={onClickUpdate}
    />
  );
};

export default SbiShinseiBankCard;
