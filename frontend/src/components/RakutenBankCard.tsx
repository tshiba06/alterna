import { type FC } from 'react';
import BaseCard from './BaseCard';

interface RakutenBankCardProps {
  total: number;
  loading: boolean;
  onClickUpdate: () => void;
}

export const RakutenBankCard: FC<RakutenBankCardProps> = ({ total, loading, onClickUpdate }) => {
  return (
    <BaseCard
      title="楽天銀行"
      bgColor="#bf0000"
      total={total}
      loading={loading}
      onClickUpdate={onClickUpdate}
    />
  );
};

export default RakutenBankCard;
